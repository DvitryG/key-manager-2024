//
//  CustomButton.swift
//  iOS
//

import SwiftUI

struct CustomButtonStyle: ButtonStyle {
    let color: Color
    let textColor: Color
    let width: CGFloat
    let height: CGFloat

    init(color: Color, textColor: Color = .white, width: CGFloat = 360, height: CGFloat = 32) {
        self.color = color
        self.textColor = textColor
        self.width = width
        self.height = height
    }

    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .frame(width: width, height: height)
            .background(color)
            .cornerRadius(10)
            .foregroundColor(textColor)
            .bold()
    }
}

extension Button {
    func customButtonStyle(color: Color, textColor: Color = .white, width: CGFloat = 360, height: CGFloat = 32) -> some View {
        self.buttonStyle(CustomButtonStyle(color: color, textColor: textColor, width: width, height: height))
    }
}

