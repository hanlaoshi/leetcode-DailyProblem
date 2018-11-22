#-------------岁月Node.js---------------------
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function (n) {
  let res = [];
  for(let i = 1; i <= n; i++) {
    let temp = BST(1, n, i, []);
    res = res.concat(temp);
  }
  return res;
};

function BST(left, right, root, leafNode) {
  let leftLeaf = [];
  let rightLeaf = [];
  leafNode = [];
  if(root - left > 0) {
    for(let i = left; i < root; i++) {
      leftLeaf = leftLeaf.concat(BST(left, root - 1, i, leafNode));
    }
  } else {
    leftLeaf = [ null ];
  }

  if(right - root > 0) {
    for(let i = root + 1; i <= right; i++) {
      rightLeaf = rightLeaf.concat(BST( root + 1, right, i, leafNode));
    }
  } else {
    rightLeaf = [ null ];
  }

  for(let i = 0; i < leftLeaf.length; i++) {
    for(let j = 0; j < rightLeaf.length; j++) {
      let node = createLeaf(root);
      node.left = leftLeaf[i];
      node.right = rightLeaf[j];
      leafNode.push(node);
    }
  }
  return leafNode;
}

function createLeaf(val) {
  return new TreeNode(val);
}
