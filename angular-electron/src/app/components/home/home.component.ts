import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Constants } from '../../constants/constants';
import { HttpService } from '../../providers/http.service';

const TONE_EXPRESION = {
  "joy": "bx--tag--ibm",
  "anger": "bx--tag--experimental",
  "fear": "bx--tag--private",
  "sadness": "bx--tag--dedicated",
  "analytical": "bx--tag--local",
  "confident": "bx--tag--third-party",
  "tentative": "bx--tag--beta"
}
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  @ViewChild('videoFile') videoFile: ElementRef;
  fileInput: any;
  isDisabled: boolean = true;

  sttData: any = [];
  toneData: any = [];

  constructor(private http: HttpService) { }

  ngOnInit() {}

  setFile(value) {
    this.fileInput = value.target.files[0];
    this.isDisabled = false;
  }

  removeSelection() {
    this.fileInput = null;
    this.videoFile.nativeElement.value = "";
    this.isDisabled = true;
  }

  getTone(tone) {
    return "btx--tag " + TONE_EXPRESION[tone];
  }

  analyzeData() {
    this.http.get('stt').subscribe((res) => {
      this.sttData = res.body['response'].response;
      this.http.get('tone').subscribe((res) => {
        this.toneData = res.body['sentences_tone'];
      })
    });
  }
}
