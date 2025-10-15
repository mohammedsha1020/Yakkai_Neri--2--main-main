// Fix static paths and navigation in newly created EJS files
const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, '../templates');
const filesToFix = ['wellness.ejs', 'therapy.ejs', 'women-seniors.ejs', 'Workshops.ejs', 'hr-register.ejs'];

function fixTemplate(content) {
  // Fix CSS paths
  content = content.replace(/href="css\//g, 'href="/static/css/');
  content = content.replace(/href="\.\.\/css\//g, 'href="/static/css/');
  
  // Fix JS paths
  content = content.replace(/src="js\//g, 'src="/static/js/');
  content = content.replace(/src="\.\.\/js\//g, 'src="/static/js/');
  
  // Fix image paths
  content = content.replace(/src="images\//g, 'src="/static/images/');
  content = content.replace(/src="\.\.\/images\//g, 'src="/static/images/');
  
  // Fix navigation .html links
  content = content.replace(/href="index\.html"/g, 'href="/"');
  content = content.replace(/href="wellness\.html"/g, 'href="/wellness"');
  content = content.replace(/href="therapy\.html"/g, 'href="/therapy"');
  content = content.replace(/href="professional\.html"/g, 'href="/professional"');
  content = content.replace(/href="workshops\.html"/g, 'href="/workshops"');
  content = content.replace(/href="courses\.html"/g, 'href="/courses"');
  content = content.replace(/href="contact\.html"/g, 'href="/contact"');
  content = content.replace(/href="corporate-yoga\.html"/g, 'href="/corporate-yoga"');
  content = content.replace(/href="meet-the-trainer\.html"/g, 'href="/meet-the-trainer"');
  content = content.replace(/href="women-wellness\.html"/g, 'href="/women-wellness"');
  content = content.replace(/href="women-seniors\.html"/g, 'href="/women-seniors"');
  content = content.replace(/href="admin\.html"/g, 'href="/admin"');
  
  return content;
}

function processFiles() {
  let count = 0;
  
  filesToFix.forEach(fileName => {
    const filePath = path.join(templatesDir, fileName);
    
    if (fs.existsSync(filePath)) {
      let content = fs.readFileSync(filePath, 'utf8');
      const originalContent = content;
      
      content = fixTemplate(content);
      
      if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Fixed: ${fileName}`);
        count++;
      } else {
        console.log(`ℹ️  No changes needed: ${fileName}`);
      }
    } else {
      console.log(`❌ File not found: ${fileName}`);
    }
  });
  
  console.log(`\n✅ Fixed ${count} files!`);
}

if (require.main === module) {
  processFiles();
}

module.exports = { fixTemplate, processFiles };
