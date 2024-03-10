//
//  ProfileView.swift
//  iOS
//


import SwiftUI

struct ProfileView: View {
    @State private var fullName: String = ""
    @State private var password: String = ""
    @State private var oldPassword: String = ""
    @State private var newPassword: String = ""
    @State private var isEditingPassword = false

    var body: some View {
        VStack {
            Text("Профиль")
                .font(.title)

            VStack(spacing: 20) {
                // TextField для ФИО
                TextField("ФИО", text: $fullName)
                    .customTFStyle()

                // SecureField для пароля
                SecureField("Пароль", text: $password)
                    .customTFStyle()

                // Кнопка "Сохранить изменения"
                Button("Сохранить изменения") {
                    saveChanges()
                }
                .customButtonStyle(color: .blue, textColor: .white)

                // SecureField для старого пароля
                VStack {
                    Text("Старый пароль")
                        .font(.subheadline)
                        .foregroundColor(.gray)

                    SecureField("Введите старый пароль", text: $oldPassword)
                        .customTFStyle()
                }
                .padding(.top, 20)

                // SecureField для нового пароля
                VStack {
                    Text("Новый пароль")
                        .font(.subheadline)
                        .foregroundColor(.gray)

                    SecureField("Введите новый пароль", text: $newPassword)
                        .customTFStyle()
                }

                // Кнопка "Сменить пароль"
                Button("Сменить пароль") {
                    isEditingPassword.toggle()
                }
                .customButtonStyle(color: .green, textColor: .white)
            }
            .padding(.horizontal, 20)
            .textFieldStyle(RoundedBorderTextFieldStyle())

            Spacer()
        }
        .padding(.top, 50)
        .sheet(isPresented: $isEditingPassword) {
            // Можете добавить экран для смены пароля, который будет отображаться в модальном окне
            //ChangePasswordView()
        }
    }

    func saveChanges() {
        // Обработка сохранения изменений
    }
}

struct ProfileView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileView()
    }
}


