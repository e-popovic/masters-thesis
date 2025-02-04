import {Component} from '@angular/core';
import * as FileSaver from "file-saver";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'image-eval';
  imgSrcA = '';
  imgSrcB = '';
  valueSlider = 50;
  progressValue = 0;
  i = 0;
  results = [''];
  startScreen = true;
  personalInfo = false;
  message = false;
  greyScreen = false;
  infoAge = '';
  infoSex = '';
  infoColorSight = '';
  messageText = "Hvala!";
  variants = [
    '0-h+10', '0-h+23','0-s+30','0-s-30',
    '1-h-8', '1-h-17','1-s+40','1-s-40',
    '2-h+7', '2-h+15','2-s+30','2-s-30',
    '4-h-9', '4-h-18','4-s+30','4-s-30',
    '5-h+5', '5-h+15','5-s+20','5-s-20',
    '6-h-8', '6-h-18','6-s+40','6-s-30',
    '7-h-8', '7-h-18','7-s+30','7-s-30',
    '8-h-15', '8-h-30','8-s+50','8-s-50',
    '9-h+15', '9-h+30','9-s+20','9-s-30',
    '10-h-8', '10-h-15','10-s+30','10-s-30',
    '11-h-8', '11-h-15','11-s+30','11-s-30',
    '12-h-8', '12-h-15','12-s+30','12-s-20',
  ];

  // show personal info form
  fillPersonalInfo() {
    this.startScreen = false;
    this.personalInfo = true;
  }

  // save personal info, randomize the order of image sets and begin presenting them
  start() {
    // uncomment next line to input duplicate image sets into the evaluation
    //this.createDuplicateSets(2);
    this.shuffle(this.variants);
    this.results.push(this.infoAge + '/' + this.infoSex + '/' + this.infoColorSight + "\n");
    this.personalInfo = false;
    // noinspection JSIgnoredPromiseFromCall
    this.presentImages();
  }

  // present image sets and save evaluation results to .txt file
  async presentImages() {
    for (const element of this.variants) {
      let original = element.split('-')[0];
      let imagesrcs = [element, original];
      this.shuffle(imagesrcs);
      this.i++;
      this.progressValue = this.i/this.variants.length * 100;
      this.imgSrcA = 'assets/images/' + imagesrcs[0] + '.jpg';
      this.imgSrcB = 'assets/images/' + imagesrcs[1] + '.jpg';
      await this.delay(15000);
      this.greyScreen = true;
      await this.delay(4000);
      this.results.push(imagesrcs[0] + ':' + imagesrcs[1] + '|' + this.valueSlider.toString() + "\n");
      this.valueSlider = 50;
      this.greyScreen = false;
      if (element === this.variants[this.variants.length-1]) {
        this.message = true;
      }
    }
    let blob = new Blob(this.results,{type:"text/plain;charset=utf-8"});
    let answerFile = 'eval-odgovori-' + Date.now() + '.txt';
    FileSaver.saveAs(blob, answerFile);
  }

  // repeat noOfDuplicates random sets (to check observer credibility)
  createDuplicateSets(noOfDuplicates: number) {
    for (let i = 0; i < noOfDuplicates; i++) {
      let index =  Math.floor(Math.random() * this.variants.length);
      this.variants.splice(index, 1);
      index = Math.floor(Math.random() * this.variants.length);
      this.variants.push(this.variants[index]);
    }
  }

  // wait for ms seconds
  delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
  }

  // Fisher–Yates shuffle algorithm for the array a
  shuffle(a: Array<String>) {
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

}
