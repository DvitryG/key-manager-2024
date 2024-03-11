//
//  Pages.swift
//  iOS
//

import SwiftUI

enum Page: String, Identifiable {
    case authStart, main, signIn, registration, createOrder
    
    var id: String {
        self.rawValue
    }
}
