//
//  CreateOrderView.swift
//  iOS
//
//  Created by HITSStudent on 10.03.2024.
//

import SwiftUI

struct CreateOrderView: View {
    
    @EnvironmentObject private var coordinator: Coordinator
    
    var body: some View {
        List {
            Button("Pop") {
                coordinator.pop()
            }
            Button("Pop to root") {
                coordinator.popToRoot()
            }
        }
        .navigationTitle("🥕")
    }
}

struct CreateOrderView_Previews: PreviewProvider {
    static var previews: some View {
        CreateOrderView()
    }
}
