//
//  RequestsViewModel.swift
//  iOS
//

import Foundation

class RequestsViewModel: ObservableObject {
    @Published var requests: [Request] = []

    init() {
        // Ваши данные могут быть получены из сети, базы данных и т.д.
        // Здесь приведен пример заполнения массива данными
        self.requests = [
            Request(number: "101", title: "Заявка 1", startTime: "10:00", endTime: "12:00", status: "на рассмотрении"),
            Request(number: "102", title: "Заявка 2", startTime: "13:00", endTime: "15:00", status: "одобрена"),
            Request(number: "103", title: "Заявка 3", startTime: "16:00", endTime: "18:00", status: "заблокирована"),
            Request(number: "104", title: "Заявка 4", startTime: "16:00", endTime: "18:00", status: "одобрена"),
            Request(number: "104", title: "Заявка 5", startTime: "18:00", endTime: "20:00", status: "одобрена"),
            Request(number: "101", title: "Заявка 6", startTime: "16:00", endTime: "18:00", status: "на рассмотрении"),
            // ... добавьте остальные заявки
        ]
    }
}
