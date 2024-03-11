//
//  AuthStartViewModel.swift
//  iOS
//

import SwiftUI

class AuthStartViewModel: ObservableObject {
    @Published var isLoggedIn = false
    @Published var showRegistration = false
    @Published var showSignIn = false

    func register() {
        showRegistration = true
    }

    func signIn() {
        showSignIn = true
    }
}
