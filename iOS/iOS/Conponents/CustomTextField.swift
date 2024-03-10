//
//  CustomTextField.swift
//  iOS
//

import SwiftUI

struct TFStyleViewModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .frame(maxWidth: .infinity)
            .overlay(RoundedRectangle(cornerRadius: 10)
                .stroke(Color.gray.opacity(0.95), lineWidth: 1))
    }
}

extension View {
    func customTFStyle() -> some View {
        modifier(TFStyleViewModifier())
    }
}
