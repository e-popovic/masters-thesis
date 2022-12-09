import {Component} from '@angular/core';
import * as FileSaver from "file-saver";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'image-eval';
  imgSrc = '';
  imgTitle = '';
  evalAllowed = false;
  valueA = 50;
  valueB = 50;
  results = ['']
  startScreen = true;

  start() {
    this.startScreen = false;
    // noinspection JSIgnoredPromiseFromCall
    this.presentImages();
  }

  async presentImages() {
    for (let i = 1; i < 3; i++) {     //  promjenjivo, broj orig Image
      let variants = ['-h', '-s'];    // promjenjivo, varijante promjena
      this.shuffle(variants);

      for (const element of variants) {
        this.evalAllowed = false;
        this.valueA = this.valueB = 50;
        let imagesrcs = [i.toString(), i.toString()+element];
        this.shuffle(imagesrcs);

        this.imgTitle = 'Image A';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[0] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '-';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Image B';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[1] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '-';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Image A';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[0] + '.png';
        this.evalAllowed = true;
        await this.delay(3000);   // 10000

        this.imgTitle = '-';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Image B';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[1] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '-';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(3000);   // 5000 (5-11 s)

        this.results.push(imagesrcs[0] + '|' + imagesrcs[1] + ":" + (this.valueA - this.valueB).toString() + "\n");
      }
    }
    let blob = new Blob(this.results,{type:"text/plain;charset=utf-8"});
    FileSaver.saveAs(blob, "evaluation-results.txt");
  }

  delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
  }

  //https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array
  //Fisher–Yates shuffle algorithm
  shuffle(a: Array<String>) {
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }


}
