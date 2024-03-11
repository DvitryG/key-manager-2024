//
//  RegistrationView.swift
//  iOS
//

import SwiftUI
import Alamofire

struct RegistrationView: View {

    @EnvironmentObject private var coordinator: Coordinator
    @StateObject private var viewModel = RegistrationViewModel()
    @StateObject private var authManager = AuthManager()

    var body: some View {
        List {
            TextField("Username", text: $viewModel.username)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            TextField("Email", text: $viewModel.email)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            SecureField("Password", text: $viewModel.password)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            SecureField("Repeat password", text: $viewModel.repeatPassword)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button("Register") {
                viewModel.registerUser { result in
                    handleRegistrationResult(result)
                }
                self.authManager.login()
                print("\n\nauthManager.register()\n\n")
            }
            .padding()
        }
        .navigationTitle("SignUp")
    }

    private func handleRegistrationResult(_ result: Result<RegistrationResponse, Error>) {
        switch result {
        case .success(let response):
            print("Registration successful. Access Token: \(response.access_token)")
            
        case .failure(let error):
            print("Registration failed. Error: \(error.localizedDescription)")
        }
    }
}

struct RegistrationView_Previews: PreviewProvider {
    static var previews: some View {
        RegistrationView()
    }
}
