package baekjoon.Math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * packageName   : baekjoon.Math
 * Author        : imhyeong-gyu
 * Data          : 2025. 1. 7.
 * Description   :
 */
class Node{
    char value;
    Node left, right;

    public Node(char value) {
        this.value = value;
    }
}

public class _1991 {

    public static int N;
    public static StringBuilder sb = new StringBuilder();
    static Map<Character, Node> tree = new HashMap<>();

    static void preOrder(Node node) {
        if (node == null) return;
        System.out.print(node.value);
        preOrder(node.left);
        preOrder(node.right);
    }

    // 중위 순회
    static void inOrder(Node node) {
        if (node == null) return;
        inOrder(node.left);           // 왼쪽 자식 방문
        System.out.print(node.value);  // 부모 노드 출력
        inOrder(node.right);          // 오른쪽 자식 방문
    }

    // 후위 순회
    static void postOrder(Node node) {
        if (node == null) return;
        postOrder(node.left);         // 왼쪽 자식 방문
        postOrder(node.right);        // 오른쪽 자식 방문
        System.out.print(node.value);  // 부모 노드 출력
    }



    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        //트리 구성
        for (int i=0; i< N; i++){
            String[] input = br.readLine().split(" ");
            char root = input[0].charAt(0);
            char left = input[1].charAt(0);
            char right = input[2].charAt(0);

            tree.putIfAbsent(root, new Node(root));
            if (left != '.'){
                tree.putIfAbsent(left, new Node(left));
                tree.get(root).left = tree.get(left);
            }

            if (right != '.') {
                tree.putIfAbsent(right, new Node(right)); // 오른쪽 자식 노드가 없으면 추가
                tree.get(root).right = tree.get(right);  // 현재 노드의 오른쪽 자식으로 연결
            }

        }

        Node root = tree.get('A');

        preOrder(root);
        System.out.println();  // 개행
        inOrder(root);
        System.out.println();  // 개행
        postOrder(root);
        System.out.println();  // 개행

    }
}
