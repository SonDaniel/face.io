import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { Constants } from '../../constants/constants';

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

  sttData: any = Constants.stt_response.response;
  toneData: any = Constants.tone_response.response.sentences_tone;

  constructor() { }

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

  }
}
