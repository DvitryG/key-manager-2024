//
//  RequestCardView.swift
//  iOS
//

import SwiftUI

struct RequestCardView: View {
    let number: String
    let title: String
    let startTime: String
    let endTime: String
    let status: String
    let onCancel: () -> Void

    var body: some View {
        VStack(spacing: 8) {
            Text("Кабинет \(number)")
                .font(.headline)

            Text("Время: \(startTime) - \(endTime)")
                .font(.subheadline)

            Divider()

            HStack {
                Text("Статус: \(status)")
                    .foregroundColor(getStatusColor())
                Spacer()
                Button(action: {
                    onCancel()
                }) {
                    Text("Отменить")
                        .foregroundColor(.red)
                }
            }
        }
        .frame(width: 360, height: 100)
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
    }

    private func getStatusColor() -> Color {
        switch status {
        case "одобрена":
            return .green
        case "на рассмотрении":
            return .orange
        case "заблокирована":
            return .red
        default:
            return .black
        }
    }
}

struct RequestCardView_Previews: PreviewProvider {
    static var previews: some View {
        RequestCardView(number: "101", title: "Заявка на аренду", startTime: "10:00", endTime: "12:00", status: "на рассмотрении", onCancel: {})
    }
}

