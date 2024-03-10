//
//  SignUpView.swift
//  iOS
//

import SwiftUI

struct SignUpView: View {
    
    @EnvironmentObject private var coordinator: Coordinator
    
    var body: some View {
        List {
            Button("Регистрация") {
                coordinator.push(.main)
            }
            Button("Войти") {
                coordinator.push(.signIn)
            }
        }
        .navigationTitle("SignUp")
    }
}

struct BananaView_Previews: PreviewProvider {
    static var previews: some View {
        SignUpView()
    }
}

