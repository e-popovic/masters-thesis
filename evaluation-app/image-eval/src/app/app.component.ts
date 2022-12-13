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
  progressValue = 0;
  i = -1;
  results = [''];
  startScreen = true;
  message = false;
  messageText = "Sljedeći set:";
  variants: String[] = [];

  start() {
    let mods = ['-h', '-sl', '-sh'];    // promjenjivo, varijante promjena
    for (let i = 0; i < 2; i++) {   //  promjenjivo, broj orig Image
      for (const mod of mods) {
        this.variants.push(i.toString()+mod);
      }
    }
    this.shuffle(this.variants);

    this.startScreen = false;
    // noinspection JSIgnoredPromiseFromCall
    this.presentImages();
  }

  async presentImages() {

    for (const element of this.variants) {
      let original = element.charAt(0);
      let imagesrcs = [original, element];
      this.shuffle(imagesrcs);

      this.i++;
      this.progressValue = this.i/this.variants.length * 100;

      this.imgSrc = 'assets/images/' + imagesrcs[0] + '.jpg';
      this.imgTitle = 'Slika A';
      await this.delay(3000);   // 8000

      this.imgTitle = '-';
      this.imgSrc = 'assets/images/grey.png';
      await this.delay(1000);   // 3000

      this.imgSrc = 'assets/images/' + imagesrcs[1] + '.jpg';
      this.imgTitle = 'Slika B';
      await this.delay(3000);   // 8000

      this.imgTitle = '-';
      this.imgSrc = 'assets/images/grey.png';
      await this.delay(3000);   // 8000

      this.evalAllowed = false;
      this.results.push(imagesrcs[0] + '|' + imagesrcs[1] + ":" + (this.valueA - this.valueB).toString() + "\n");
      this.valueA = this.valueB = 50;

      if (element === this.variants[this.variants.length-1]) {
        this.messageText = "Hvala!";
        this.message = true;
      }
      else {
        this.message = true;
        await this.delay(2000);
        this.message = false;
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
