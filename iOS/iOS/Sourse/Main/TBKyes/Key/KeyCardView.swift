//
//  KeyCardView.swift
//  iOS
//
//  Created by HITSStudent on 10.03.2024.
//

import SwiftUI

struct MyKeyCardView: View {
    let key: MyKey

    var body: some View {
        VStack(spacing: 8) {
            Text("Ключ от \(key.cabinetNumber)")
                .font(.headline)

            Text("Вернуть до \(key.returnDate)")
                .font(.subheadline)

            Divider()

            switch key.status {
            case .onHand:
                Button("Передать") {
                    // Обработка передачи ключа
                }
            case .transferred(let from):
                HStack {
                    Button("Подтверждаю") {
                        // Обработка подтверждения получения
                    }
                    Button("Отмена") {
                        // Обработка отмены
                    }
                }
            }
        }
        .frame(width: 360, height: 100)
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
    }
}

struct MyKeyCardView_Previews: PreviewProvider {
    static var previews: some View {
        MyKeyCardView(key: MyKey(cabinetNumber: "101", returnDate: "10:00 15 марта", status: .onHand))
    }
}


