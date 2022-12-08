import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'image-eval';
  imgSrc = '';
  imgTitle = '';

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

  async presentImages() {
    for (let i = 1; i < 3; i++) {     //  promjenjivo, broj orig slika
      let variants = ['-h', '-s'];    // promjenjivo, varijante promjena
      this.shuffle(variants);

      for (const element of variants) {
        let imagesrcs = [i.toString(), i.toString()+element];
        this.shuffle(imagesrcs);

        this.imgTitle = 'Picture A';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[0] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Picture B';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[1] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Picture A';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[0] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(1000);   // 3000

        this.imgTitle = 'Picture B';
        this.imgSrc = 'assets/images/'+ i.toString() + '/' + imagesrcs[1] + '.png';
        await this.delay(3000);   // 10000

        this.imgTitle = '';
        this.imgSrc = 'assets/images/grey.png';
        await this.delay(3000);   // 5000 (5-11 s)

      }


    }
  }

  ngOnInit() {
    // noinspection JSIgnoredPromiseFromCall
    this.presentImages();
  }
}
