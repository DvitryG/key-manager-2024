//
//  Request.swift
//  iOS
//

import Foundation

struct Request: Identifiable {
    let id = UUID()
    let number: String
    let title: String
    let startTime: String
    let endTime: String
    let status: String
}
