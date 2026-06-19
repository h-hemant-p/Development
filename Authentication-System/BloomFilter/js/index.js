const fs = require('fs');
const crypto = require('crypto');
const path = require('path');

class BloomFilter {
    constructor(size = 1000, numHashes = 1, fileName = 'bloom_filter.txt') {
        this.size = size;
        this.numHashes = numHashes;
        this.fileName = fileName;
        this.bitArray = Array(size).fill(0);
        this.currentPath = process.cwd();
        this.loadFilter();
    }

    _hashes(value) {
        const hashValues = [];
        for (let i = 0; i < this.numHashes; i++) {
            const hash = crypto.createHash('sha256')
                .update(`${value}${i}`)
                .digest('hex');
            const hashValue = parseInt(hash, 16) % this.size;
            hashValues.push(hashValue);
        }
        return hashValues;
    }

    add(value) {
        const hashValues = this._hashes(value);
        for (const hashValue of hashValues) {
            this.bitArray[hashValue] = 1;
        }
    }

    check(value) {
        const hashValues = this._hashes(value);
        for (const hashValue of hashValues) {
            if (this.bitArray[hashValue] === 1) {
                return true;
            }
        }
        return false;
    }

    saveFilter() {
        const filePath = path.join(this.currentPath, this.fileName);
        const bitArrayString = this.bitArray.join('');
        fs.writeFileSync(filePath, bitArrayString, 'utf8');
    }

    loadFilter() {
        const filePath = path.join(this.currentPath, this.fileName);
        if (fs.existsSync(filePath)) {
            const bitArrayString = fs.readFileSync(filePath, 'utf8');
            this.bitArray = bitArrayString.split('').map(Number);
        }
    }
}

// Example usage
const bloomFilter = new BloomFilter(1000, 1);

const email = "hemant";
console.log(bloomFilter.check(email));
// Uncomment below lines to test adding and saving
bloomFilter.add(email);
bloomFilter.saveFilter();

