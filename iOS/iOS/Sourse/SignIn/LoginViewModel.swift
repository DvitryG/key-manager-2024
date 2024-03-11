//
//  SignInViewModel.swift
//  iOS
//
//  Created by HITSStudent on 11.03.2024.
//

import SwiftUI
import Alamofire

class LoginViewModel: ObservableObject {
    @Published var email = ""
    @Published var password = ""
    
    func loginUser(completion: @escaping (Result<LoginResponse, Error>) -> Void) {
        let model = LoginModel(email: email, password: password)

        NetworkManager.shared.loginUser(model: model) { result in
            switch result {
            case .success(let response):
                print("Received login response: \(response)")
                completion(.success(response))
            case .failure(let error):
                print("Login failed. Error: \(error.localizedDescription)")
                completion(.failure(error))
            }
        }
    }
}
