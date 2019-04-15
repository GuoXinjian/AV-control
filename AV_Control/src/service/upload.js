import fs from "fs"
import path from "path"
export function uploadImage(file) {
  var fileNameArr = file.originalname.split('.');
  var suffix = fileNameArr[fileNameArr.length - 1];
  let imageName = `${Date.now()}.${suffix}`;
  fs.renameSync(path.join(__dirname, '../uploads/' + file.filename), path.join(__dirname, `../images/${imageName}`));
  file['newfilename'] = `${file.filename}.${suffix}`;
  return imageName;
}