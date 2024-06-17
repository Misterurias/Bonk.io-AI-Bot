const LZString = require('lz-string');

class bytebuffer2 {
  constructor() {
    this.index = 0;
    this.buffer = null;
    this.view = null;
  }

  readByte() {
    const value = this.view.getUint8(this.index);
    this.index += 1;
    return value;
  }

  readInt() {
    const value = this.view.getInt32(this.index);
    this.index += 4;
    return value;
  }

  readShort() {
    const value = this.view.getInt16(this.index);
    this.index += 2;
    return value;
  }

  readUint() {
    const value = this.view.getUint32(this.index);
    this.index += 4;
    return value;
  }

  readBoolean() {
    return this.readByte() === 1;
  }

  readDouble() {
    const value = this.view.getFloat64(this.index);
    this.index += 8;
    return value;
  }

  readFloat() {
    const value = this.view.getFloat32(this.index);
    this.index += 4;
    return value;
  }

  readUTF() {
    const length = this.readShort();
    let utfString = '';
    for (let i = 0; i < length; i++) {
      utfString += String.fromCharCode(this.readByte());
    }
    return utfString;
  }

  fromBase64(base64) {
    const binaryString = Buffer.from(base64, 'base64').toString('binary');
    const length = binaryString.length;
    const bytes = new Uint8Array(length);
    for (let i = 0; i < length; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    this.buffer = bytes.buffer;
    this.view = new DataView(this.buffer);
    this.index = 0;
  }
}

function decodeFromDatabase(map) {
  const b64mapdata = LZString.decompressFromEncodedURIComponent(map);
  const binaryReader = new bytebuffer2();
  binaryReader.fromBase64(b64mapdata);

  const decodedMap = { 
    v: 1, 
    s: { re: false, nc: false, pq: 1, gd: 25, fl: false }, 
    physics: { shapes: [], fixtures: [], bodies: [], bro: [], joints: [], ppm: 12 }, 
    spawns: [], 
    capZones: [], 
    m: { a: "noauthor", n: "noname", dbv: 2, dbid: -1, authid: -1, date: "", rxid: 0, rxn: "", rxa: "", rxdb: 1, cr: [], pub: false, mo: "" }
  };

  try {
    decodedMap.v = binaryReader.readShort();
    if (decodedMap.v > 15) {
      throw new Error("Future map version, please refresh page");
    }
    decodedMap.s.re = binaryReader.readBoolean();
    decodedMap.s.nc = binaryReader.readBoolean();
    if (decodedMap.v >= 3) {
      decodedMap.s.pq = binaryReader.readShort();
    }
    if (decodedMap.v >= 4 && decodedMap.v <= 12) {
      decodedMap.s.gd = binaryReader.readShort();
    } else if (decodedMap.v >= 13) {
      decodedMap.s.gd = binaryReader.readFloat();
    }
    if (decodedMap.v >= 9) {
      decodedMap.s.fl = binaryReader.readBoolean();
    }
    decodedMap.m.rxn = binaryReader.readUTF();
    decodedMap.m.rxa = binaryReader.readUTF();
    decodedMap.m.rxid = binaryReader.readUint();
    decodedMap.m.rxdb = binaryReader.readShort();
    decodedMap.m.n = binaryReader.readUTF();
    decodedMap.m.a = binaryReader.readUTF();
    if (decodedMap.v >= 10) {
      decodedMap.m.vu = binaryReader.readUint();
      decodedMap.m.vd = binaryReader.readUint();
    }
    if (decodedMap.v >= 4) {
      const crLength = binaryReader.readShort();
      for (let i = 0; i < crLength; i++) {
        decodedMap.m.cr.push(binaryReader.readUTF());
      }
    }
    if (decodedMap.v >= 5) {
      decodedMap.m.mo = binaryReader.readUTF();
      decodedMap.m.dbid = binaryReader.readInt();
    }
    if (decodedMap.v >= 7) {
      decodedMap.m.pub = binaryReader.readBoolean();
    }
    if (decodedMap.v >= 8) {
      decodedMap.m.dbv = binaryReader.readInt();
    }
    decodedMap.physics.ppm = binaryReader.readShort();
    const broLength = binaryReader.readShort();
    for (let i = 0; i < broLength; i++) {
      decodedMap.physics.bro[i] = binaryReader.readShort();
    }
    const shapesLength = binaryReader.readShort();
    for (let i = 0; i < shapesLength; i++) {
      const shapeType = binaryReader.readShort();
      if (shapeType === 1) {
        const shape = { type: "bx", w: 10, h: 40, c: [0, 0], a: 0.0, sk: false };
        shape.w = binaryReader.readDouble();
        shape.h = binaryReader.readDouble();
        shape.c = [binaryReader.readDouble(), binaryReader.readDouble()];
        shape.a = binaryReader.readDouble();
        shape.sk = binaryReader.readBoolean();
        decodedMap.physics.shapes.push(shape);
      } else if (shapeType === 2) {
        const shape = { type: "ci", r: 25, c: [0, 0], sk: false };
        shape.r = binaryReader.readDouble();
        shape.c = [binaryReader.readDouble(), binaryReader.readDouble()];
        shape.sk = binaryReader.readBoolean();
        decodedMap.physics.shapes.push(shape);
      } else if (shapeType === 3) {
        const shape = { type: "po", v: [], s: 1, a: 0, c: [0, 0] };
        shape.s = binaryReader.readDouble();
        shape.a = binaryReader.readDouble();
        shape.c = [binaryReader.readDouble(), binaryReader.readDouble()];
        const verticesLength = binaryReader.readShort();
        for (let j = 0; j < verticesLength; j++) {
          shape.v.push([binaryReader.readDouble(), binaryReader.readDouble()]);
        }
        decodedMap.physics.shapes.push(shape);
      }
    }
    const fixturesLength = binaryReader.readShort();
    for (let i = 0; i < fixturesLength; i++) {
      const fixture = { sh: 0, n: "Def Fix", fr: 0.3, fp: null, re: 0.8, de: 0.3, f: 0x4f7cac, d: false, np: false, ng: false };
      fixture.sh = binaryReader.readShort();
      fixture.n = binaryReader.readUTF();
      fixture.fr = binaryReader.readDouble();
      if (fixture.fr === Number.MAX_VALUE) {
        fixture.fr = null;
      }
      const fpType = binaryReader.readShort();
      if (fpType === 0) {
        fixture.fp = null;
      } else if (fpType === 1) {
        fixture.fp = false;
      } else if (fpType === 2) {
        fixture.fp = true;
      }
      fixture.re = binaryReader.readDouble();
      if (fixture.re === Number.MAX_VALUE) {
        fixture.re = null;
      }
      fixture.de = binaryReader.readDouble();
      if (fixture.de === Number.MAX_VALUE) {
        fixture.de = null;
      }
      fixture.f = binaryReader.readUint();
      fixture.d = binaryReader.readBoolean();
      fixture.np = binaryReader.readBoolean();
      if (decodedMap.v >= 11) {
        fixture.ng = binaryReader.readBoolean();
      }
      if (decodedMap.v >= 12) {
        fixture.ig = binaryReader.readBoolean();
      }
      decodedMap.physics.fixtures.push(fixture);
    }
    const bodiesLength = binaryReader.readShort();
    for (let i = 0; i < bodiesLength; i++) {
      const body = { type: "s", n: "Unnamed", p: [0, 0], a: 0, fric: 0.3, fricp: false, re: 0.8, de: 0.3, lv: [0, 0], av: 0, ld: 0, ad: 0, fr: false, bu: false, cf: { x: 0, y: 0, w: true, ct: 0 }, fx: [], f_c: 1, f_p: true, f_1: true, f_2: true, f_3: true, f_4: true, fz: { on: false, x: 0, y: 0, d: true, p: true, a: true, t: 0, cf: 0 }};
      body.type = binaryReader.readUTF();
      body.n = binaryReader.readUTF();
      body.p = [binaryReader.readDouble(), binaryReader.readDouble()];
      body.a = binaryReader.readDouble();
      body.fric = binaryReader.readDouble();
      body.fricp = binaryReader.readBoolean();
      body.re = binaryReader.readDouble();
      body.de = binaryReader.readDouble();
      body.lv = [binaryReader.readDouble(), binaryReader.readDouble()];
      body.av = binaryReader.readDouble();
      body.ld = binaryReader.readDouble();
      body.ad = binaryReader.readDouble();
      body.fr = binaryReader.readBoolean();
      body.bu = binaryReader.readBoolean();
      body.cf.x = binaryReader.readDouble();
      body.cf.y = binaryReader.readDouble();
      body.cf.ct = binaryReader.readDouble();
      body.cf.w = binaryReader.readBoolean();
      body.f_c = binaryReader.readShort();
      body.f_1 = binaryReader.readBoolean();
      body.f_2 = binaryReader.readBoolean();
      body.f_3 = binaryReader.readBoolean();
      body.f_4 = binaryReader.readBoolean();
      if (decodedMap.v >= 2) {
        body.f_p = binaryReader.readBoolean();
      }
      if (decodedMap.v >= 14) {
        body.fz.on = binaryReader.readBoolean();
        if (body.fz.on) {
          body.fz.x = binaryReader.readDouble();
          body.fz.y = binaryReader.readDouble();
          body.fz.d = binaryReader.readBoolean();
          body.fz.p = binaryReader.readBoolean();
          body.fz.a = binaryReader.readBoolean();
          if (decodedMap.v >= 15) {
            body.fz.t = binaryReader.readShort();
            body.fz.cf = binaryReader.readDouble();
          }
        }
      }
      const fxLength = binaryReader.readShort();
      for (let j = 0; j < fxLength; j++) {
        body.fx.push(binaryReader.readShort());
      }
      decodedMap.physics.bodies.push(body);
    }
    const spawnsLength = binaryReader.readShort();
    for (let i = 0; i < spawnsLength; i++) {
      const spawn = { x: 400, y: 300, xv: 0, yv: 0, priority: 5, r: true, f: true, b: true, gr: false, ye: false, n: "Spawn" };
      spawn.x = binaryReader.readDouble();
      spawn.y = binaryReader.readDouble();
      spawn.xv = binaryReader.readDouble();
      spawn.yv = binaryReader.readDouble();
      spawn.priority = binaryReader.readShort();
      spawn.r = binaryReader.readBoolean();
      spawn.f = binaryReader.readBoolean();
      spawn.b = binaryReader.readBoolean();
      spawn.gr = binaryReader.readBoolean();
      spawn.ye = binaryReader.readBoolean();
      spawn.n = binaryReader.readUTF();
      decodedMap.spawns.push(spawn);
    }
    const capZonesLength = binaryReader.readShort();
    for (let i = 0; i < capZonesLength; i++) {
      const capZone = { n: "Cap Zone", ty: 1, l: 10, i: -1 };
      capZone.n = binaryReader.readUTF();
      capZone.l = binaryReader.readDouble();
      capZone.i = binaryReader.readShort();
      if (decodedMap.v >= 6) {
        capZone.ty = binaryReader.readShort();
      }
      decodedMap.capZones.push(capZone);
    }
    const jointsLength = binaryReader.readShort();
    for (let i = 0; i < jointsLength; i++) {
      const jointType = binaryReader.readShort();
      let joint;
      if (jointType === 1) {
        joint = { type: "rv", d: { la: 0, ua: 0, mmt: 0, ms: 0, el: false, em: false, cc: false, bf: 0, dl: true }, aa: [0, 0] };
        joint.d.la = binaryReader.readDouble();
        joint.d.ua = binaryReader.readDouble();
        joint.d.mmt = binaryReader.readDouble();
        joint.d.ms = binaryReader.readDouble();
        joint.d.el = binaryReader.readBoolean();
        joint.d.em = binaryReader.readBoolean();
        joint.aa = [binaryReader.readDouble(), binaryReader.readDouble()];
      } else if (jointType === 2) {
        joint = { type: "d", d: { fh: 0, dr: 0, cc: false, bf: 0, dl: true }, aa: [0, 0], ab: [0, 0] };
        joint.d.fh = binaryReader.readDouble();
        joint.d.dr = binaryReader.readDouble();
        joint.aa = [binaryReader.readDouble(), binaryReader.readDouble()];
        joint.ab = [binaryReader.readDouble(), binaryReader.readDouble()];
      } else if (jointType === 3) {
        joint = { type: "lpj", d: { cc: false, bf: 0, dl: true }, pax: 0, pay: 0, pa: 0, pf: 0, pl: 0, pu: 0, plen: 0, pms: 0 };
        joint.pax = binaryReader.readDouble();
        joint.pay = binaryReader.readDouble();
        joint.pa = binaryReader.readDouble();
        joint.pf = binaryReader.readDouble();
        joint.pl = binaryReader.readDouble();
        joint.pu = binaryReader.readDouble();
        joint.plen = binaryReader.readDouble();
        joint.pms = binaryReader.readDouble();
      } else if (jointType === 4) {
        joint = { type: "lsj", d: { cc: false, bf: 0, dl: true }, sax: 0, say: 0, sf: 0, slen: 0 };
        joint.sax = binaryReader.readDouble();
        joint.say = binaryReader.readDouble();
        joint.sf = binaryReader.readDouble();
        joint.slen = binaryReader.readDouble();
      } else if (jointType === 5) {
        joint = { type: "g", n: "", ja: -1, jb: -1, r: 1 };
        joint.n = binaryReader.readUTF();
        joint.ja = binaryReader.readShort();
        joint.jb = binaryReader.readShort();
        joint.r = binaryReader.readDouble();
      }
      if (jointType !== 5) {
        joint.ba = binaryReader.readShort();
        joint.bb = binaryReader.readShort();
        joint.d.cc = binaryReader.readBoolean();
        joint.d.bf = binaryReader.readDouble();
        joint.d.dl = binaryReader.readBoolean();
      }
      decodedMap.physics.joints.push(joint);
    }
  } catch (error) {
    console.error('Failed to decode map data:', error);
    throw error;
  }

  return decodedMap;
}

module.exports = {
    decodeFromDatabase
  };
