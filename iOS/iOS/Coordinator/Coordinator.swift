//
//  Coordinator.swift
//  iOS
//

import SwiftUI

class Coordinator: ObservableObject {
    
    @Published var path = NavigationPath()
    @Published var fullScreenCover: FullScreenCover?
    
    func push(_ page: Page) {
        path.append(page)
    }
    
    func pop() {
        path.removeLast()
    }
    
    func popToRoot() {
        path.removeLast(path.count)
    }
    
    func present(fullScreenCover: FullScreenCover) {
        self.fullScreenCover = fullScreenCover
    }
    
    @ViewBuilder
    func build(page: Page) -> some View {
        switch page {
        case .authStart:
            AuthStartView()
        case .main:
            MainView()
        case .signIn:
            LoginView()
        case .registration:
            RegistrationView()
        case .createOrder:
            CreateOrderView()
        }
    }
}
