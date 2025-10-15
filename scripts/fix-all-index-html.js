const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, '..', 'templates');

// Get all .ejs files
const files = fs.readdirSync(templatesDir).filter(file => file.endsWith('.ejs'));

let totalReplacements = 0;

files.forEach(file => {
  const filePath = path.join(templatesDir, file);
  let content = fs.readFileSync(filePath, 'utf8');
  let modified = false;
  
  // Replace index.html with / (for home links)
  const beforeCount = (content.match(/href="index\.html"/g) || []).length;
  if (beforeCount > 0) {
    content = content.replace(/href="index\.html"/g, 'href="/"');
    modified = true;
    console.log(`✓ ${file}: Replaced ${beforeCount} instance(s) of href="index.html"`);
    totalReplacements += beforeCount;
  }
  
  // Replace index.html#contact with /#contact (for contact links with hash)
  const beforeHashCount = (content.match(/href="index\.html#contact"/g) || []).length;
  if (beforeHashCount > 0) {
    content = content.replace(/href="index\.html#contact"/g, 'href="/#contact"');
    modified = true;
    console.log(`✓ ${file}: Replaced ${beforeHashCount} instance(s) of href="index.html#contact"`);
    totalReplacements += beforeHashCount;
  }
  
  if (modified) {
    fs.writeFileSync(filePath, content, 'utf8');
  }
});

console.log(`\n✅ Total replacements: ${totalReplacements}`);
console.log('✅ All index.html references fixed!');
