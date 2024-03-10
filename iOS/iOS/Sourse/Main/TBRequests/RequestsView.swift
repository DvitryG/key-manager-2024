//
//  RequestsView.swift
//  iOS
//

import SwiftUI

struct RequestsView: View {
    @StateObject private var viewModel = RequestsViewModel()

    var body: some View {
        List(viewModel.requests) { request in
            RequestCardView(
                number: request.number,
                title: request.title,
                startTime: request.startTime,
                endTime: request.endTime,
                status: request.status,
                onCancel: {
                }
            )
            .listRowInsets(EdgeInsets())
        }
        .navigationTitle("Заявки")
        .onAppear {
        }
    }
}



struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        
        RequestsView()
    }
}

