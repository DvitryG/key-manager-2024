//
//  AuthStartView.swift
//  iOS
//

import SwiftUI

struct AuthStartView: View {
    @EnvironmentObject private var coordinator: Coordinator
    
    var body: some View {
        VStack {
            Text("Добро пожаловать!")
            Button("Зарегистрироваться") {
                coordinator.push(.registration)
            }
            .padding()
            
            Button("Войти") {
                coordinator.push(.signIn)
            }
            .padding()
        }
    }
}

struct AuthStartView_Previews: PreviewProvider {
    static var previews: some View {
        AuthStartView()
    }
}
