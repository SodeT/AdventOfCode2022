const std = @import("std");
const os = std.os;
const assert = std.debug.assert;
const reader = std.io.reader.readUntilDelimiterOrEof;

pub fn main() !void {
    @setRuntimeSafety(false);
    //const stdout = std.io.getStdOut().writer();

    var myScore: u32 = 0;

    var file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        
        myScore += getScore(line);

    }
        std.debug.print("{}\n", .{myScore});
}

fn getScore(match: []u8) u32 {
    var myScore: u32 = 0;
    var oponentScore: u32 = 0; 

    myScore = switch(match[2]) {
        'X' => 1,
        'Y' => 2,
        'Z' => 3,
        else => 0,
    };

    oponentScore = switch(match[0]) {
        'A' => 1,
        'B' => 2,
        'C' => 3,
        else => 0,
    };

    if (myScore == 1) {
        if (oponentScore == 1) {
            myScore += 3;
        } else if (oponentScore == 2) {
            myScore += 0;
        } else if (oponentScore == 3) {
            myScore += 6;
        }
    } else if (myScore == 2) {
        if (oponentScore == 1) {
            myScore += 6;
        } else if (oponentScore == 2) {
            myScore += 3;
        } else if (oponentScore == 3) {
            myScore += 0;
        }
    } else if (myScore == 3) {
        if (oponentScore == 1) {
            myScore += 0;
        } else if (oponentScore == 2) {
            myScore += 6;
        } else if (oponentScore == 3) {
            myScore += 3;
        }
    }
    return myScore;
}