//
//  Key.swift
//  iOS
//
//  Created by HITSStudent on 10.03.2024.
//

import Foundation

struct MyKey: Identifiable {
    let id = UUID()
    let cabinetNumber: String
    let returnDate: String
    let status: MyKeyStatus
}

enum MyKeyStatus {
    case onHand
    case transferred(from: String)
}
