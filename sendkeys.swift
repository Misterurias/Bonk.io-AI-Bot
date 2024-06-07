// import Foundation
// import Quartz

// let src = CGEventSource(stateID: CGEventSourceStateID.hidSystemState)

// func sendKey(key: CGKeyCode, keyDown: Bool, toPid pid: pid_t) {
//     let event = CGEvent(keyboardEventSource: src, virtualKey: key, keyDown: keyDown)
//     print("Sending key \(key) \(keyDown ? "down" : "up") to pid \(pid)")
//     event?.postToPid(pid)
//     print("Key event posted")
// }

// guard CommandLine.arguments.count == 4 else {
//     print("Usage: sendkeys <pid> <key> <true|false>")
//     exit(1)
// }

// let pid = Int32(CommandLine.arguments[1])!
// let key = CGKeyCode(Int(CommandLine.arguments[2])!)
// let keyDown = CommandLine.arguments[3] == "true"

// sendKey(key: key, keyDown: keyDown, toPid: pid)

import Foundation
import ApplicationServices

func sendKeyEvent(_ keyCode: Int, keyDown: Bool, toPid pid: Int) {
    guard let src = CGEventSource(stateID: .hidSystemState) else {
        print("Failed to create event source")
        return
    }
    
    let keyEvent = CGEvent(keyboardEventSource: src, virtualKey: CGKeyCode(keyCode), keyDown: keyDown)
    keyEvent?.postToPid(pid_t(pid))
}

if CommandLine.argc != 4 {
    print("Usage: sendkeys <pid> <keycode> <true|false>")
    exit(1)
}

guard let pid = Int(CommandLine.arguments[1]),
      let keyCode = Int(CommandLine.arguments[2]),
      let keyDown = Bool(CommandLine.arguments[3]) else {
    print("Invalid arguments")
    exit(1)
}

sendKeyEvent(keyCode, keyDown: keyDown, toPid: pid)
