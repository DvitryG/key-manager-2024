//
//  LoginView.swift
//  iOS
//

import SwiftUI

struct LoginView: View {
    @EnvironmentObject private var coordinator: Coordinator
    @StateObject private var viewModel = LoginViewModel()

    var body: some View {
        List {
            TextField("Email", text: $viewModel.email)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            SecureField("Password", text: $viewModel.password)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("Login") {
                viewModel.loginUser { result in
                    // Выводим в консоль результат входа
                    switch result {
                    case .success(let response):
                        print("Login successful. Access Token: \(response.access_token)")
                        // Переходим на .main после успешного входа
                        coordinator.push(.main)
                    case .failure(let error):
                        print("Login failed. Error: \(error.localizedDescription)")
                    }
                }
            }
            .padding()
        }
        .navigationTitle("Login")
    }
}


struct SignInView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
    }
}

