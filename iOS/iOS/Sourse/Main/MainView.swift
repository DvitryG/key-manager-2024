//
//  MainView.swift
//  iOS
//

import SwiftUI

struct MainView: View {
    
    var body: some View {
        TabView {
            RequestsView()
                .tabItem {
                    Label("Заявки", systemImage: "list.bullet.rectangle")
                }
            
            MyKeysView()
                .tabItem {
                    Label("Мои ключи", systemImage: "key")
                }
            
            ProfileView()
                .tabItem {
                    Label("Аккаунт", systemImage: "person")
                }
        }
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        MainView()
    }
}

