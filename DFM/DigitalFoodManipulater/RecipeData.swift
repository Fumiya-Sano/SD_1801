//
//  RecipeData.swift
//  DigitalFoodManipulater
//
//  Created by 小田将也 on 2018/10/20.
//  Copyright © 2018年 Jenove_ze. All rights reserved.
//

import Foundation
import UIKit

class RecipeData {
    var name: String = ""
    var url: String = ""
    var imageurl: String = ""
    
    init(name: String, url: String, imageurl: String) {
        self.name = name
        self.url = url
        self.imageurl = imageurl
    }
    
    class ImageInfo: Codable {
        private enum CodingKeys: String, CodingKey {
            case medium = "Medium"
        }
        
        var medium: String?
        
    }
    var imageInfo: ImageInfo = ImageInfo()

}

