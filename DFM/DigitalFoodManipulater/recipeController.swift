//
//  recipeController.swift
//  DigitalFoodManipulater
//
//  Created by 佐野文哉 on 2018/10/20.
//  Copyright © 2018年 Jenove_ze. All rights reserved.
//

import UIKit
import Foundation




class recipeController: UITableViewController {
    
    var recipeDataArray = [RecipeData]() //ここにSyoJasuからもらってきたURLなどを入れる
    var imageCache = NSCache<AnyObject, UIImage>()
    var recipename = "おつまみに！タラモ春巻き"
    var pageurl = "https://recipe.rakuten.co.jp/recipe/1170006099/"
    var imageurl = "https://image.space.rakuten.co.jp/d/strg/ctrl/3/e02b25d40463829442f1b0cec17231ef015e6962.94.2.3.2.jpg"
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false
        var recipe = RecipeData(name: "とっても簡単！☆茄子とトマトのミートグラタン☆", url: "https://recipe.rakuten.co.jp/recipe/1490005189/", imageurl: "https://image.space.rakuten.co.jp/d/strg/ctrl/3/ed46001aa6b3af354c0d34dd0243f468a6524761.32.2.3.2.jpg")
        recipeDataArray.append(recipe)
        recipe = RecipeData(name: "きゅうりとトマトのクリームチーズサラダ", url: "https://recipe.rakuten.co.jp/recipe/1390012080/", imageurl: "https://image.space.rakuten.co.jp/d/strg/ctrl/3/28671b9a30a3212c3c9101aeeb58701964834315.92.2.3.2.jpg")
        recipeDataArray.append(recipe)
        recipe = RecipeData(name: "沖縄の味★タコライス", url: "https://recipe.rakuten.co.jp/recipe/1370002492/", imageurl: "https://image.space.rakuten.co.jp/d/strg/ctrl/3/37a3b25623256e1f557a839c98ac3f447ea0ab8a.07.2.3.2.jpg")
        recipeDataArray.append(recipe)
        recipe = RecipeData(name: "トマト＆チーズの簡単オムレツ♪", url: "https://recipe.rakuten.co.jp/recipe/1500001531/", imageurl: "https://image.space.rakuten.co.jp/d/strg/ctrl/3/49451ae9d72d67adbe137a1c15e3b3b0053e084e.10.2.3.2.jpg")
        recipeDataArray.append(recipe)


        
        
        
        
        
        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItemself.editButtonItem
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return recipeDataArray.count
    }


    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "recipeCell", for: indexPath) as? RecipeTableViewCell else {
            return UITableViewCell()
        }
        let recipeData = recipeDataArray[indexPath.row]
        cell.recipeTitleLabel.text = recipeData.name
        cell.recipeUrl = recipeData.url
        cell.recipeImageView.image = UIImage(url: URL(string: recipeData.imageurl))
        print("image")
        return cell
    }
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let cell = sender as? RecipeTableViewCell {
            if let recipeUrlController = segue.destination as? recipeUrlController {
                recipeUrlController.recipeUrl = cell.recipeUrl!
            }
        }
    }
    @IBAction func returnTop(segue: UIStoryboardSegue){
        
    }

}

extension UIImage {
    convenience init?(url: URL?) {
        guard let url = url else { return nil }
        
        do {
            let data = try Data(contentsOf: url)
            self.init(data: data)
        } catch {
            print("Cannot load image from url: \(url) with error: \(error)")
            return nil
        }
    }
}
