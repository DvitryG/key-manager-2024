//
//  TransferKeyView.swift
//  iOS
//

import SwiftUI

struct TransferKeyView: View {
    @State private var searchQuery: String = ""
    @State private var selectedUser: String?

    var body: some View {
        VStack {
            TextField("Поиск по имени", text: $searchQuery)
                .customTFStyle()
                .padding()

            if searchQuery.isEmpty {
                Text("Введите имя")
                    .foregroundColor(.red)
                    .padding(.top, 5)
            } else {
               
            }

            Spacer()

            HStack {
                Button("Отмена") {
                    // Добавьте код для отмены операции передачи ключа
                }
                .customButtonStyle(color: .gray, textColor: .white)

                Spacer()

                Button("Подтвердить") {
                    if let selectedUser = selectedUser {
                        // Добавьте код для подтверждения передачи ключа выбранному пользователю
                    }
                }
                .customButtonStyle(color: .green, textColor: .white)
            }
            .padding()
        }
        .navigationTitle("Передать ключ")
    }
}

struct TransferKeyView_Previews: PreviewProvider {
    static var previews: some View {
        TransferKeyView()
    }
}
