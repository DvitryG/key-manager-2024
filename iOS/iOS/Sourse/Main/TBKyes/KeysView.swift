//
//  KeysView.swift
//  iOS
//

import SwiftUI

struct MyKeysView: View {
    @StateObject private var viewModel = MyKeysViewModel()

    var body: some View {
        List(viewModel.keys) { key in
            MyKeyCardView(key: key)
                .listRowInsets(EdgeInsets())
        }
        .navigationTitle("Мои ключи")
    }
}


struct MyKeysView_Previews: PreviewProvider {
    static var previews: some View {
        MyKeysView()
    }
}
