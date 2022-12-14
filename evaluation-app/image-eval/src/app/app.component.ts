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
  valueA = 50;
  valueB = 50;
  progressValue = 0;
  i = 0;
  results = [''];
  startScreen = true;
  message = false;
  messageText = "Sljedeći set:";
  variants = [
    '0-h+5', '0-h+10','0-s+30','0-s-30',
    '1-h+5', '1-h+15','1-s+40','1-s-40',
    '2-h-10', '2-h+10','2-s+30','2-s-30',
    '3-h+5', '3-h+10','3-s+40','3-s-40',
    '4-h+15', '4-h-15','4-s+30','4-s-30',
    '5-h+5', '5-h+15','5-s+20','5-s-20',
    '6-h-5', '6-h-15','6-s+40','6-s-30',
    '7-h-5', '7-h-15','7-s+30','7-s-30',
    '8-h-10', '8-h-20','8-s+50','8-s-50',
    '9-h+10', '9-h-20','9-s+20','9-s-30',
  ];

  start() {
    //this.createDuplicateSets(2);
    this.shuffle(this.variants);

    this.startScreen = false;
    // noinspection JSIgnoredPromiseFromCall
    this.presentImages();
  }

  async presentImages() {

    for (const element of this.variants) {
      let original = element.charAt(0);
      let imagesrcs = [element, original];
      this.shuffle(imagesrcs);

      this.i++;
      this.progressValue = this.i/this.variants.length * 100;

      this.imgSrc = 'assets/images/' + imagesrcs[0] + '.jpg';
      this.imgTitle = 'Slika A';
      await this.delay(3000);   // 8000

      this.imgTitle = '-';
      this.imgSrc = 'assets/images/grey.jpg';
      await this.delay(1000);   // 3000

      this.imgSrc = 'assets/images/' + imagesrcs[1] + '.jpg';
      this.imgTitle = 'Slika B';
      await this.delay(3000);   // 8000

      this.imgTitle = '-';
      this.imgSrc = 'assets/images/grey.jpg';
      await this.delay(3000);   // 8000

      this.results.push(imagesrcs[0] + ':' + imagesrcs[1] + '|' + this.valueA.toString()
        + ':' + this.valueB.toString() + "\n");
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

  // check observer credibility by repeating random sets
  createDuplicateSets(noOfDuplicates: number) {
    for (let i = 0; i < noOfDuplicates; i++) {
      let index =  Math.floor(Math.random() * this.variants.length);
      this.variants.splice(index, 1);
      index = Math.floor(Math.random() * this.variants.length);
      this.variants.push(this.variants[index]);
    }
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
