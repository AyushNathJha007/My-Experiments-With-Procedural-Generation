using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class LevelBuilder : MonoBehaviour
{
    // Start is called before the first frame update
    public Sprite[] BuilderElements;
    public GameObject DummyBlock;
    char[] SymbolArray = { 'G', 'S', 'B', '#', '#', 'F', 'P', '?', '#', '#', '*', 'P', 'P', 'P', '#', '?', 'G', 'S', 'B', 'P', 'P', 'P', 'P', 'P', 'P' };
    public Transform parentOfWorld;
    void Start()
    {
        readTextFile("Assets/MarioLevelGenerator/LevelBuilderScript/GenLev1_upRight.txt");
    }

    

    void readTextFile(string file_path)
    {
        StreamReader inp_stm = new StreamReader(file_path);
        float x = 0, y = 0;
        int i = 0;
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
             foreach(char c in inp_ln)
            {
                char upChar = char.ToUpper(c);
                GameObject block = Instantiate(DummyBlock, new Vector3(x, y, 0.0f), Quaternion.identity, parentOfWorld);
                for (int j=0;j<25;j++)
                {
                   
                    if (upChar==SymbolArray[j])
                    {

                        block.gameObject.GetComponent<SpriteRenderer>().sprite = BuilderElements[j];
                        break;
                    }
                }
                x += 0.822f;

            }
            x = 0;
            y -= 0.822f;
        }

    inp_stm.Close();
    }
}
