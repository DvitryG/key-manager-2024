//
//  RegistrationResponse.swift
//  iOS
//

struct RegistrationResponse: Decodable {
    let access_token: String
    let token_type: String

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        access_token = try container.decode(String.self, forKey: .access_token)
        token_type = try container.decode(String.self, forKey: .token_type)
    }

    private enum CodingKeys: String, CodingKey {
        case access_token
        case token_type
    }
}


