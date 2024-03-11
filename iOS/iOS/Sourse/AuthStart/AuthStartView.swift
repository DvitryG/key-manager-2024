//
//  AuthStartView.swift
//  iOS
//

import SwiftUI




struct AuthStartView: View {
    @ObservedObject var viewModel = AuthStartViewModel()
    @EnvironmentObject var coordinator: Coordinator

    var body: some View {
        VStack {
            Text("Добро пожаловать!")

            if !viewModel.isLoggedIn {
                Button("Зарегистрироваться") {
                    coordinator.push(.registration)
                }
                .padding()

                Button("Войти") {
                    coordinator.push(.signIn)
                }
                .padding()
            }

           
            if viewModel.isLoggedIn {
                Button("Продолжить") {
                    coordinator.push(.main)
                }
                .padding()
            }
        }
    }
}

struct AuthStartView_Previews: PreviewProvider {
    static var previews: some View {
        AuthStartView()
    }
}
