//
//  main.swift
//  RandomlyGenerate69420
//
//  Created by Baran Önen on 22.07.2020.
//  Copyright © 2020 Baran Önen. All rights reserved.
//

import Foundation

print("Randomly Generate 69420")
print("This program will generate random 5-digit numbers until it generates 69420")
print("To start, type y")

let answer = readLine()

if answer == "y" {
    var trialnumber = 0
    var number = 0
    
    while number != 69420 {
        number = Int.random(in: 10000 ... 99999)
        print("\(number)")
        trialnumber = trialnumber + 1
    }

    print("Done in \(trialnumber) tries")

}

