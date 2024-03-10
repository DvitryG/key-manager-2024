//
//  Pages.swift
//  iOS
//

import SwiftUI

enum Page: String, Identifiable {
    case main, signIn, signUp, createOrder
    
    var id: String {
        self.rawValue
    }
}
