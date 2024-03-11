//
//  LoginView.swift
//  iOS
//

import SwiftUI

struct LoginView: View {
    @EnvironmentObject private var coordinator: Coordinator
    @StateObject private var viewModel = LoginViewModel()
    @StateObject private var authManager = AuthManager()

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
                    switch result {
                    case .success(let response):
                        print("Login successful. Access Token: \(response.access_token)")
                        self.authManager.login()
                        print("\n\nauthManager.login()\n\n")
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

