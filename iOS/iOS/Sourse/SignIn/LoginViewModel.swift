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
    @Published var isLoggedIn = false // Переменная для отслеживания состояния авторизации

    func loginUser(completion: @escaping (Result<LoginResponse, Error>) -> Void) {
        let model = LoginModel(email: email, password: password)

        NetworkManager.shared.loginUser(model: model) { result in
            switch result {
            case .success(let response):
                // Опционально: Выводим в консоль данные после успешного входа
                print("Received login response: \(response)")

                // Обновляем переменную isLoggedIn и вызываем completion
                self.isLoggedIn = true
                completion(.success(response))
            case .failure(let error):
                // Выводим в консоль ошибку
                print("Login failed. Error: \(error.localizedDescription)")

                // Вызываем completion с ошибкой
                completion(.failure(error))
            }
        }
    }
}
