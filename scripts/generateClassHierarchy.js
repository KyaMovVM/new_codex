const fs = require('fs');

function generateClass(def, parent) {
  const lines = [];
  const extendsPart = parent ? ` extends ${parent}` : '';
  lines.push(`class ${def.name}${extendsPart} {`);
  if (Array.isArray(def.methods)) {
    for (const method of def.methods) {
      lines.push(`  ${method}() {}`);
    }
  }
  lines.push('}');
  lines.push('');
  if (Array.isArray(def.children)) {
    for (const child of def.children) {
      lines.push(generateClass(child, def.name));
    }
  }
  return lines.join('\n');
}

if (require.main === module) {
  const [,, inputPath, outputPath] = process.argv;
  if (!inputPath || !outputPath) {
    console.error('Usage: node generateClassHierarchy.js <input.json> <output.js>');
    process.exit(1);
  }
  const data = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
  const result = generateClass(data, null);
  fs.writeFileSync(outputPath, result, 'utf8');
}

module.exports = generateClass;
