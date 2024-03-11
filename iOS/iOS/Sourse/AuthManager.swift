//
//  AuthManager.swift
//  iOS
//

import Foundation

class AuthManager: ObservableObject {
    @Published var isAuthorized: Bool {
        didSet {
            saveAuthState()
        }
    }

    init() {
        self.isAuthorized = UserDefaults.standard.bool(forKey: "isAuthorized")
    }

    func login() {
        isAuthorized = true
    }

    func logout() {
        isAuthorized = false
    }

    private func saveAuthState() {
        UserDefaults.standard.set(isAuthorized, forKey: "isAuthorized")
        if UserDefaults.standard.synchronize() {
            print("Saved auth state successfully")
        } else {
            print("Failed to save auth state")
        }
    }
}
