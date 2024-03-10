//
//  KeysViewModel.swift
//  iOS
//

import Foundation

class MyKeysViewModel: ObservableObject {
    @Published var keys: [MyKey] = []

    init() {
        self.keys = [
            MyKey(cabinetNumber: "101", returnDate: "10:00 15 марта", status: .onHand),
            MyKey(cabinetNumber: "102", returnDate: "подтвердите получение", status: .transferred(from: "John Doe")),
        ]
    }
}

