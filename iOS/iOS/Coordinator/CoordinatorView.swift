//
//  CoordinatorView.swift
//  iOS
//

import SwiftUI

struct CoordinatorView: View {
    
    @StateObject private var coordinator = Coordinator()
    @StateObject private var authManager = AuthManager()
    var body: some View {
        NavigationStack(path: $coordinator.path) {
            coordinator.build(page: pageSelector())
                .navigationDestination(for: Page.self) { page in
                    coordinator.build(page: page)
                }
                
        }
        .environmentObject(coordinator)
    }
    
    private func pageSelector() -> Page {
        return authManager.isAuthorized ? .main : .authStart
    }
}

struct CoordinatorView_Previews: PreviewProvider {
    static var previews: some View {
        CoordinatorView()
    }
}

