#!/usr/bin/swift

import Foundation

/*
 * Complete the findPoint function below.
 */
func findPoint(px: Int, py: Int, qx: Int, qy: Int) -> [Int] {
    /*
     * Write your code here.
     */
    let xDelta = qx - px
    let yDelta = qy - py
    let rx = xDelta + qx
    let ry = yDelta + qy
    var r = [Int]()
    r.append(rx)
    r.append(ry)
    return r
}
print(1)
let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for _ in 1...n {
    guard let pxPyQxQyTemp = readLine() else { fatalError("Bad input") }
    let pxPyQxQy = pxPyQxQyTemp.split(separator: " ").map{ String($0) }

    guard let px = Int(pxPyQxQy[0].trimmingCharacters(in: .whitespacesAndNewlines))
    else { fatalError("Bad input") }

    guard let py = Int(pxPyQxQy[1].trimmingCharacters(in: .whitespacesAndNewlines))
    else { fatalError("Bad input") }

    guard let qx = Int(pxPyQxQy[2].trimmingCharacters(in: .whitespacesAndNewlines))
    else { fatalError("Bad input") }

    guard let qy = Int(pxPyQxQy[3].trimmingCharacters(in: .whitespacesAndNewlines))
    else { fatalError("Bad input") }

    let result = findPoint(px: px, py: py, qx: qx, qy: qy)

    fileHandle.write(result.map{ String($0) }.joined(separator: " ").data(using: .utf8)!)
    fileHandle.write("\n".data(using: .utf8)!)
}


