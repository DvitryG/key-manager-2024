//
//  NetworkManager.swift
//  iOS
//

import Alamofire

class NetworkManager {
    static let shared = NetworkManager()
    
    private init() {}
    
    func registerUser(model: RegistrationModel, completion: @escaping (Result<RegistrationResponse, Error>) -> Void) {
        let url = "http://0.0.0.0:5500/users/register"
        let parameters: [String: Any] = [
            "name": model.username,
            "password": model.password,
            "email": model.email,
            "repeat_password": model.repeatPassword
        ]
        
        AF.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .responseDecodable(of: RegistrationResponse.self) { response in
                switch response.result {
                case .success(let registrationResponse):
                    completion(.success(registrationResponse))
                case .failure(let error):
                    completion(.failure(error))
                }
            }
    }
    
    func loginUser(model: LoginModel, completion: @escaping (Result<LoginResponse, Error>) -> Void) {
        let url = "http://0.0.0.0:5500/users/login"
        
        let parameters: [String: Any] = [
            "email": model.email,
            "password": model.password
        ]

        AF.request(url, method: .post, parameters: parameters, encoding: JSONEncoding.default)
            .validate()
            .responseDecodable(of: LoginResponse.self) { response in
                debugPrint(response)

                switch response.result {
                case .success(let loginResponse):
                    completion(.success(loginResponse))
                case .failure(let error):
                    completion(.failure(error))
                }
            }

    }
    
}

