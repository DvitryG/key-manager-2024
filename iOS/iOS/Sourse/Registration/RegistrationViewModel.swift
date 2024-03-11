//
//  RegistrationViewModel.swift
//  iOS
//

import SwiftUI
import Alamofire

class RegistrationViewModel: ObservableObject {
    @Published var username = ""
    @Published var email = ""
    @Published var password = ""
    @Published var repeatPassword = ""

    private var networkManager: NetworkManager

    init(networkManager: NetworkManager = NetworkManager.shared) {
        self.networkManager = networkManager
    }

    func registerUser(completion: @escaping (Result<RegistrationResponse, Error>) -> Void) {
        guard password == repeatPassword else {
            completion(.failure(NSError(domain: "YourAppDomain", code: 1001, userInfo: [NSLocalizedDescriptionKey: "Passwords do not match"])))
            return
        }

        let registrationModel = RegistrationModel(username: username, email: email, password: password, repeat_password: repeatPassword)

        networkManager.registerUser(model: registrationModel, completion: completion)
    }
}
