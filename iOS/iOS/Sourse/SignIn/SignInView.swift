//
//  SignInView.swift
//  iOS
//

import SwiftUI

struct SignInView: View {
    
    @EnvironmentObject private var coordinator: Coordinator
    
    var body: some View {
        List {
            Button("Войти") {
                coordinator.push(.main)
            }
            Button("Регистрация") {
                coordinator.push(.signUp)
            }
        }
        .navigationTitle("SignIn")
    }
}

struct SignInView_Previews: PreviewProvider {
    static var previews: some View {
        SignInView()
    }
}

