package nl.tudelft.jpacman.board;

import static org.assertj.core.api.Assertions.assertThat;

import nl.tudelft.jpacman.sprite.PacManSprites;

import org.junit.jupiter.api.Test;

public class BoardFactoryTest {
    /*
     * - BoardFactory(PacManSprites)
     * - createBoard(Square[][])
     */
    private static final PacManSprites pms = new PacManSprites();
    private final BoardFactory boardFac = new BoardFactory(pms);
    private final Square s1 = new BasicSquare();
    private final Square s2 = new BasicSquare();

    @Test
    void testCreateBoard(){
        assertThat(boardFac.createBoard(new Square[][]{{s1}, {s2}})).isNotNull();
    }
}
